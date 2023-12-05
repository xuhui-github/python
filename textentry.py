import wx
import MySQLdb
MySQLdb.
if __name__ =='__main__':
    app = wx.PySimpleApp()
    choices = ["Alpha", "Baker", "Charlie", "Delta"]
    dialog = wx.SingleChoiceDialog(None, "Pick a word","Choices", choices)
    if dialog.ShowModal() == wx.ID_OK:
        print( "You select %s\n" % dialog.GetStringSelection())
    dialog.Destroy()
    
