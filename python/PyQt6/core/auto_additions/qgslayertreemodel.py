# The following has been generated automatically from src/core/layertree/qgslayertreemodel.h
QgsLayerTreeModel.ShowLegend = QgsLayerTreeModel.Flag.ShowLegend
QgsLayerTreeModel.ShowLegendAsTree = QgsLayerTreeModel.Flag.ShowLegendAsTree
QgsLayerTreeModel.DeferredLegendInvalidation = QgsLayerTreeModel.Flag.DeferredLegendInvalidation
QgsLayerTreeModel.UseEmbeddedWidgets = QgsLayerTreeModel.Flag.UseEmbeddedWidgets
QgsLayerTreeModel.UseTextFormatting = QgsLayerTreeModel.Flag.UseTextFormatting
QgsLayerTreeModel.AllowNodeReorder = QgsLayerTreeModel.Flag.AllowNodeReorder
QgsLayerTreeModel.AllowNodeRename = QgsLayerTreeModel.Flag.AllowNodeRename
QgsLayerTreeModel.AllowNodeChangeVisibility = QgsLayerTreeModel.Flag.AllowNodeChangeVisibility
QgsLayerTreeModel.AllowLegendChangeState = QgsLayerTreeModel.Flag.AllowLegendChangeState
QgsLayerTreeModel.ActionHierarchical = QgsLayerTreeModel.Flag.ActionHierarchical
QgsLayerTreeModel.UseThreadedHitTest = QgsLayerTreeModel.Flag.UseThreadedHitTest
QgsLayerTreeModel.Flags = lambda flags=0: QgsLayerTreeModel.Flag(flags)
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsLayerTreeModel.Flag.__bool__ = lambda flag: bool(_force_int(flag))
QgsLayerTreeModel.Flag.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsLayerTreeModel.Flag.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsLayerTreeModel.Flag.__or__ = lambda flag1, flag2: QgsLayerTreeModel.Flag(_force_int(flag1) | _force_int(flag2))
