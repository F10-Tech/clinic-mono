Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Users\adbad\OneDrive\Desktop\clinic-mono\run.bat" & Chr(34), 0
WinScriptHost.Run Chr(34) & "C:\Users\adbad\OneDrive\Desktop\clinic-mono\front.bat" & Chr(34), 0
Set WinScriptHost = Nothing