import wx
import wx.grid

class TestFrame(wx.Fram):
    rowLabels=['uno','dos','tres','quatro','cinco']
    colLabels=['homer','marge','bart','lisa','maggie']

    def __init__(self):
        wx.Frame.__init__(self,None,title='Grid Headers', size=(500,200))
        grid=wx.grid.Grid(self)
        grid.CreateGrid(5,5)
        for row in range(5):

