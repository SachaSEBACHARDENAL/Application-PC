# Vérifie l'état du pare-feu Windows
$firewall = (Get-NetFirewallProfile | Where-Object {$_.Enabled -eq $true}).Name
Write-Host "Pare-feu activé pour : $firewall"

# Vérifie l’antivirus (Windows Defender)
$defender = Get-MpComputerStatus
Write-Host "Antivirus actif : $($defender.AntivirusEnabled)"

# Vérifie les updates
$lastUpdate = (Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 1).InstalledOn
Write-Host "Dernier update installé le : $lastUpdate"
