using Excel = Microsoft.Office.Interop.Excel;
 
private Excel.Application excelApp;
private Excel.Workbooks excelWorkbooks;
private Excel.Workbook excelWorkbook;
 
private void theEntryInTheReportFile()
{
    excelApp = new Excel.Application();
    excelApp.Visible = false;
    excelApp.SheetsInNewWorkbook = 1;
    excelApp.Workbooks.Add(Type.Missing);
    excelApp.Columns.ColumnWidth = 30;
    excelApp.Rows.RowHeight = 30;
    excelApp.DisplayAlerts = true;
 
    excelWorkbooks = _excelApp.Workbooks;
    excelWorkbook = _excelWorkbooks[1];
 
    excelWorkbook.Saved = true;
 
    excelApp.DefaultSaveFormat = Excel.XlFileFormat.xlWorkbookNormal;
 
    string path = string.Empty;
    using(SaveFileDialog saveDialog = new SaveFileDialog())
    {
         if(saveDialog.ShowDialog() == DialogResult.OK)
         {
             path = saveDialog.FileName;
             excelWorkbook.SaveAs(path);
             saveToFile(path, dataGridView1, excelApp, excelWorkbook, excelWorkbooks);
         }
    }
}
 
private Excel.Sheets excelSheets;
private Excel.Worksheet excelWorksheet;
private Excel.Range excelRange;
 
private void saveToFile(string pathToFile, DataGridView dbg,
     Excel.Application excelApp, Excel.Workbook excelWorkbook, Excel.Workbooks excelWorkbooks)
{
    try
    {
        excelSheets = excelWorkbook.Worksheets;
        excelWorksheet = (Excel.Worksheet)excelSheets.get_Item(1);
        int i,j;
 
        for(i = 0; i < dbg.Rows.Count; i++)
            for(j = 0; j < dbg.Columns.Count; j++)
            {
                excelRange = (Excel.Range)excelWorksheet.Cell[i, j];
                excelRange.Value2 = dbg.Rows[i].Cells[j].Value.ToString();
            }
    }
    catch(Exception exception)
    {
          MessageBox.Show(exception.ToString(), "Ошибка записи",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
    }
    finally
    {
          excelApp.Quit();
    }
}