$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Drawing

$root = (Get-Location).ProviderPath
$source = Join-Path $root "docs\evidence"
$target = Join-Path $root "docs\screenshots"

New-Item -ItemType Directory -Force -Path $target | Out-Null

$files = Get-ChildItem -LiteralPath $source -Filter "*.txt" | Where-Object { $_.Name -match "^[0-9]{2}-" } | Sort-Object Name

foreach ($file in $files) {
    $lines = [System.IO.File]::ReadAllLines(
        $file.FullName,
        [System.Text.Encoding]::UTF8
    )

    $width = 1500
    $height = [Math]::Max(420, 170 + $lines.Count * 30)

    $bitmap = New-Object System.Drawing.Bitmap($width, $height)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)

    $background = [System.Drawing.Color]::FromArgb(16, 24, 39)
    $foreground = [System.Drawing.Brushes]::White
    $textBrush = New-Object System.Drawing.SolidBrush(
        [System.Drawing.Color]::FromArgb(167, 243, 208)
    )

    $graphics.Clear($background)

    $titleFont = New-Object System.Drawing.Font(
        "Malgun Gothic", 23, [System.Drawing.FontStyle]::Bold
    )
    $bodyFont = New-Object System.Drawing.Font(
        "Malgun Gothic", 15
    )

    $title = $file.BaseName.Replace("-", " ")

    $graphics.DrawString(
        $title, $titleFont, $foreground, 35, 35
    )

    $y = 105

    foreach ($line in $lines) {
        $graphics.DrawString(
            $line, $bodyFont, $textBrush, 35, $y
        )
        $y += 30
    }

    $outFile = Join-Path $target ($file.BaseName + ".png")

    $outFile = [System.IO.Path]::GetFullPath($outFile)

    $bitmap.Save(
        $outFile,
        [System.Drawing.Imaging.ImageFormat]::Png
    )

    $graphics.Dispose()
    $bitmap.Dispose()
    $titleFont.Dispose()
    $bodyFont.Dispose()

    if (-not (Test-Path -LiteralPath $outFile)) {
        throw "PNG file was not created: $outFile"
    }

    Write-Host "Created: $outFile"
}

Write-Host "PNG generation completed."
