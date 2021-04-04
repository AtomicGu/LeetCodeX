"""图论编辑器
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class Node:
    """同时适用于有向图和无向图的结点类
    """
    def __init__(self, index=None):
        if index is None:
            self.index = id(self) % 100
        else:
            self.index = index
        self.tos = set()
        self.frs = set()
        return

    def __repr__(self) -> str:
        to_index = {to.index for to in self.tos}
        fr_index = {fr.index for fr in self.frs}
        return f"{self.index} -> {to_index}\n\t<- {fr_index}"

    def link_to(self, other: "Node"):
        """单向连接
        """
        self.tos.add(other)
        other.frs.add(self)
        return

    def link(self, other: "Node"):
        """双向连接
        """
        self.link_to(other)
        other.link_to(self)
        return


class UiNode:
    focus = None
    lock = None

    def __init__(self, x, y, radius, ax: plt.Axes):
        self.patch = plt.Circle((x, y), radius, lw=5, edgecolor="black")
        self.press_pos = None
        self.background = None
        self.connect(ax)

        self.outedges = {}
        # TODO 拖动结点时同时更新连线
        return

    def connect(self, ax: plt.Axes):
        ax.add_patch(self.patch)
        canvas = ax.figure.canvas
        self.cids = [
            canvas.mpl_connect('button_press_event', self.on_press),
            canvas.mpl_connect('button_release_event', self.on_release),
            canvas.mpl_connect('motion_notify_event', self.on_motion),
        ]
        return

    def disconnect(self):
        canvas = self.patch.figure.canvas
        for cid in self.cids:
            canvas.mpl_disconnect(cid)
        return

    def on_press(self, event: mpl.backend_bases.MouseEvent):
        # 检查是不是点击自己
        patch = self.patch
        ax = patch.axes
        if event.inaxes != ax or UiNode.lock is not None:
            return
        contains, attrd = patch.contains(event)
        if not contains:
            return

        if event.button == mpl.backend_bases.MouseButton.LEFT:
            # 左键双击给结点连线
            if event.dblclick:
                if UiNode.focus is None:
                    UiNode.focus = self
                    self.patch.set_edgecolor("red")
                elif UiNode.focus is self:
                    self.patch.set_edgecolor("black")
                    UiNode.focus = None
                else:
                    if self in UiNode.focus.outedges:
                        UiNode.focus.outedges[self].remove()
                        del UiNode.focus.outedges[self]
                    else:
                        x0, y0 = UiNode.focus.patch.get_center()
                        x1, y1 = self.patch.get_center()
                        _ = mpl.patches.FancyArrow(x0, y0, x1 - x0, y1 - y0)
                        ax.add_patch(_)
                        UiNode.focus.outedges[self] = _

                    UiNode.focus.patch.set_edgecolor("black")
                    UiNode.focus = None
                ax.figure.canvas.draw()

            # 左键单击拖动结点
            else:
                # 记录点击位置
                x, y = patch.get_center()
                self.press_pos = event.xdata - x, event.ydata - y
                UiNode.lock = self

                # 绘制背景并保存到缓冲区
                patch.set_animated(True)
                canvas = patch.figure.canvas
                canvas.draw()
                self.background = canvas.copy_from_bbox(ax.bbox)

                # 现在只重新绘制选中的图形
                patch.draw(canvas.get_renderer())
                canvas.blit(ax.bbox)

        # 右键点击删除结点
        elif event.button == mpl.backend_bases.MouseButton.RIGHT:
            self.patch.remove()
            if UiNode.focus is self:
                UiNode.focus = None  # 注意指针悬挂
            ax.figure.canvas.draw()
        return

    def on_motion(self, event: mpl.backend_bases.MouseEvent):
        # 检查是不是点击自己
        patch = self.patch
        ax = patch.axes
        if event.inaxes != ax or UiNode.lock is not self:
            return

        # 移动自身
        dx, dy = self.press_pos
        patch.set_center((event.xdata - dx, event.ydata - dy))

        # 重置背景
        canvas = ax.figure.canvas
        canvas.restore_region(self.background)

        # 只重新绘制当前形状
        patch.draw(canvas.get_renderer())
        canvas.blit(ax.bbox)
        return

    def on_release(self, event):
        # 检查是不是点击自己
        patch = self.patch
        ax = patch.axes
        if event.inaxes != ax or UiNode.lock is not self:
            return

        UiNode.lock = None
        patch.set_animated(False)
        patch.figure.canvas.draw()
        return

    @staticmethod
    def add_node_on_press(event: mpl.backend_bases.MouseEvent):
        # 鼠标中键添加结点
        return


fig = plt.gcf()
ax = fig.add_subplot(aspect='equal')
rects = [
    UiNode(np.random.random(), np.random.random(), 0.1, ax) for i in range(10)
]

plt.show()
