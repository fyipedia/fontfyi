# fontfyi — Python Google Fonts Metadata Library Demo
Output demo.gif

Set FontSize 20
Set Width 1000
Set Height 580
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 30ms
Set Padding 24

Type "uv run --with fontfyi python3"
Enter
Sleep 2.5s

Type "from fontfyi import info, css, pair"
Enter
Sleep 1s

Type "# Font metadata"
Enter
Sleep 0.5s

Type "info('Inter')['category']"
Enter
Sleep 1.5s

Type "# CSS import snippet"
Enter
Sleep 0.5s

Type "css('Inter')[:60]"
Enter
Sleep 1.5s

Type "# Font pairing suggestions"
Enter
Sleep 0.5s

Type "[p['name'] for p in pair('Inter')[:3]]"
Enter
Sleep 2s

Type "exit()"
Enter
Sleep 1s
