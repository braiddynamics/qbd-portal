# fix_category_labels.ps1

# Define the mapping of Folder -> Desired Sidebar Label
$categories = @{
    "docs/01-foundations"      = "1. The Foundational Principles"
    "docs/02-topology"         = "2. Topological Nature of Matter"
    "docs/03-emergent-reality" = "3. Emergent Reality"
    "docs/04-phenomenology"    = "4. Phenomenological Consequences"
    "docs/05-synthesis"        = "5. Applications and Synthesis"
    "docs/06-appendices"       = "6. Appendices"
}

# Iterate and create the _category_.yml files
foreach ($folder in $categories.Keys) {
    if (Test-Path $folder) {
        $label = $categories[$folder]
        $filePath = "$folder/_category_.yml"
        
        # Content for the category metadata
        # We explicitly set the label and position to ensure ordering
        $content = @"
label: "$label"
collapsible: true
collapsed: true
link:
  type: generated-index
  title: "$label"
"@
        
        Set-Content -Path $filePath -Value $content -Encoding UTF8
        Write-Host "Fixed Category: $folder -> '$label'" -ForegroundColor Green
    } else {
        Write-Host "Warning: Folder $folder not found." -ForegroundColor Red
    }
}