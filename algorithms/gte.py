"""图论编辑器

左键双击添加结点
右键双击删除结点

左键单击拖动结点
右键单击选中结点和连线，再次连线以取消连线

按空格键给结点统一编号
"""

from typing import List, MutableSet

import matplotlib.pyplot as plt
from matplotlib.backend_bases import KeyEvent, MouseButton, MouseEvent
from matplotlib.patches import FancyArrowPatch


class Node:
    """同时适用于有向图和无向图的结点类"""

    def __init__(self, index=None):
        if index is None:
            self.index = id(self) % 100
        else:
            self.index = index
        self.tos: MutableSet[Node] = set()
        self.frs: MutableSet[Node] = set()
        return

    def __repr__(self) -> str:
        to_index = {to.index for to in self.tos}
        fr_index = {fr.index for fr in self.frs}
        return f"{self.index} ->{to_index}\n   <-{fr_index}\n"

    def link_to(self, other: "Node"):
        """单向连接"""
        self.tos.add(other)
        other.frs.add(self)
        return

    def link(self, other: "Node"):
        """双向连接"""
        self.link_to(other)
        other.link_to(self)
        return

    def unlink_to(self, other: "Node"):
        """断开连接"""
        self.tos.discard(other)
        other.frs.discard(self)
        return


Graph_t = List[Node]  # 图就是 Node 列，每个 Node 的索引就是下标


class NodeUi:
    def __init__(self, x, y, ax: plt.Axes, *, radius=0.05, index=None):
        self.circle = plt.Circle(
            (x, y),
            radius,
            lw=2,
            edgecolor="#84affa",
            facecolor="#c6e5ff",
        )
        self.ax = ax
        ax.add_patch(self.circle)

        if index is None:
            index = str(id(self) % 100)
        self.index = plt.Text(x, y, index, size="small")
        ax.add_artist(self.index)

        self.tos = {}
        self.frs = {}
        return

    def set_selected(self):
        self.circle.set_edgecolor("red")
        return

    def set_unselected(self):
        self.circle.set_edgecolor("#84affa")
        return

    def link_to(self, other: "NodeUi"):
        if other in self.tos:
            return

        xy0 = self.circle.get_center()
        xy1 = other.circle.get_center()
        edge = FancyArrowPatch(
            xy0,
            xy1,
            arrowstyle="-|>",
            mutation_scale=20,
            shrinkB=13,
            edgecolor="#7f7f7f",
            facecolor="#7f7f7f",
            linewidth=2,
            zorder=0,
        )
        self.ax.add_patch(edge)

        self.tos[other] = edge
        other.frs[self] = edge
        return

    def unlink_to(self, other: "NodeUi"):
        edge = self.tos.pop(other, None)
        if edge is None:
            return

        other.frs.pop(self)
        edge.remove()
        return

    def get_position(self):
        return self.circle.get_center()

    def set_position(self, x, y):
        xy = (x, y)
        self.circle.set_center(xy)
        self.index.set_position(xy)
        for to, edge in self.tos.items():
            edge.set_positions(xy, to.get_position())
        for fr, edge in self.frs.items():
            edge.set_positions(fr.get_position(), xy)
        return

    def contains(self, event) -> bool:
        return self.circle.contains(event)[0]

    def set_animated(self, b: bool):
        self.circle.set_animated(b)
        self.index.set_animated(b)
        for edge in self.tos.values():
            edge.set_animated(b)
        for edge in self.frs.values():
            edge.set_animated(b)
        return

    def draw(self):
        renderer = self.ax.figure.canvas.get_renderer()
        self.circle.draw(renderer)
        self.index.draw(renderer)
        for edge in self.tos.values():
            edge.draw(renderer)
        for edge in self.frs.values():
            edge.draw(renderer)
        return

    def remove(self):
        self.circle.remove()
        self.index.remove()

        for to, edge in self.tos.items():
            to.frs.pop(self)
            edge.remove()
        self.tos = {}

        for fr, edge in self.frs.items():
            fr.tos.pop(self)
            edge.remove()
        self.frs = {}
        return

    def set_index(self, index: int):
        self.index.set_text(str(index))
        return

    def get_index(self) -> int:
        return int(self.index.get_text())


class GraphUi:
    def __init__(self, fig: plt.Figure, directed=False):
        fig.clear()
        self.fig = fig
        self.can = fig.canvas
        self.ax = fig.add_subplot(aspect="equal")

        self.directed = directed
        self.ui_nodes: List[NodeUi] = []
        self.selected = None
        return

    def connect(self):
        self.cid_press = self.can.mpl_connect(
            "button_press_event",
            self.on_press,
        )
        self.cid_key_press = self.can.mpl_connect(
            "key_press_event",
            self.on_key_press,
        )
        return

    def disconnect(self):
        self.can.mpl_disconnect(self.cid_press)
        self.can.mpl_disconnect(self.cid_key_press)
        return

    def on_press(self, event: MouseEvent):
        """鼠标事件分流"""
        if event.inaxes is not self.ax:
            return

        if event.button == MouseButton.LEFT:
            if event.dblclick:
                self.on_left_dbdown(event)
            else:
                self.on_left_down(event)
        elif event.button == MouseButton.RIGHT:
            if event.dblclick:
                self.on_right_dbdown(event)
            else:
                self.on_right_down(event)
        return

    def on_left_down(self, event: MouseEvent):
        """按下左键拖动结点"""
        focus: NodeUi = None
        for i in self.ui_nodes:
            if i.contains(event):
                focus = i
        if focus is None:
            return

        # 记录点击位置
        x, y = focus.get_position()
        dx, dy = event.xdata - x, event.ydata - y

        # 绘制背景并保存到缓冲区
        focus.set_animated(True)
        self.can.draw()
        background = self.can.copy_from_bbox(self.ax.bbox)

        # 现在只重新绘制选中的图形
        focus.draw()
        self.can.blit(self.ax.bbox)

        def on_motion(event: MouseEvent):
            if event.inaxes is not self.ax:
                return

            # 重置背景
            self.can.restore_region(background)

            # 只重新绘制当前形状
            x, y = event.xdata, event.ydata
            focus.set_position(x - dx, y - dy)
            focus.draw()
            self.can.blit(self.ax.bbox)
            return

        def on_release(event: MouseEvent):
            focus.set_animated(False)
            self.can.mpl_disconnect(cid_motion)
            self.can.mpl_disconnect(cid_release)
            self.cid_press = self.can.mpl_connect(
                "button_press_event",
                self.on_press,
            )
            self.can.draw()
            return

        # 动态注册事件处理器
        self.can.mpl_disconnect(self.cid_press)  # 可以确保同时只进行一个操作
        cid_motion = self.can.mpl_connect("motion_notify_event", on_motion)
        cid_release = self.can.mpl_connect("button_release_event", on_release)
        return

    def on_right_down(self, event):
        """按下右键结点连线"""
        focus: NodeUi = None
        for i in self.ui_nodes:
            if i.contains(event):
                focus = i
        if focus is None:
            return

        if self.selected is None:
            # 选中第一个点
            self.selected = focus
            focus.set_selected()
            self.can.draw()
            return

        if self.selected is focus:
            # 再次点击取消选中
            self.selected = None
            focus.set_unselected()
            self.can.draw()
            return

        # 断开连线
        if focus in self.selected.tos:
            self.selected.unlink_to(focus)
            if not self.directed:
                focus.unlink_to(self.selected)
        # 连线
        else:
            self.selected.link_to(focus)
            if not self.directed:
                focus.link_to(self.selected)
        self.selected.set_unselected()
        self.selected = None
        self.can.draw()
        return

    def on_left_dbdown(self, event):
        """左键双击添加结点"""
        self.ui_nodes.append(NodeUi(event.xdata, event.ydata, self.ax))
        self.can.draw()
        return

    def on_right_dbdown(self, event):
        """右键双击删除结点"""
        focus: NodeUi = None
        index = None
        for j, i in enumerate(self.ui_nodes):
            if i.contains(event):
                focus = i
                index = j
        if focus is None:
            return

        focus.remove()
        del self.ui_nodes[index]
        if self.selected is focus:
            self.selected = None
        self.can.draw()
        return

    def on_key_press(self, event: KeyEvent):
        """按空格给结点编号"""
        if event.key == " ":
            self.index_nodes()
            self.can.draw()
        return

    def index_nodes(self):
        for j, i in enumerate(self.ui_nodes):
            i.set_index(j)
        return

    def output_model(self):
        """输出数据模型"""
        self.index_nodes()
        model = [Node(i) for i in range(len(self.ui_nodes))]
        for i in self.ui_nodes:
            node = model[i.get_index()]
            for j in i.tos:
                node.link_to(model[j.get_index()])
        return model


def input_graph(directed=False) -> Graph_t:
    """输入图

    参数：
        directed (bool): 是否要求有向图，默认为否

    返回：
        Graph_t: 结点数组，其中的结点已经按下标编号
    """
    graph_ui = GraphUi(plt.gcf(), directed)
    graph_ui.connect()
    plt.show()
    return graph_ui.output_model()


if __name__ == "__main__":
    print(input_graph(True))
