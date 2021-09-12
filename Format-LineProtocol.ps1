function Format-LineProtocol {
    [CmdletBinding()]
    param (
        # The Name of the measurement
        [Parameter(mandatory)]
        [string]$MeasurementName,
        # An array of tags you may wish to add to the line item (optional)
        [Parameter()]
        [array]$Tags,
        # The name of the metric and the value of the metric you're measuring. 
        [Parameter(Mandatory)]
        [array]$Field
    )
    $output = ""
    switch ($PSBoundParameters.Keys) {
        'MeasurementName' { 
            $output += $MeasurementName 
        }
        'Tags' {
            foreach ($n in $tags.Keys) {
                $output += ("," + $n + "=" + $tags.$n)
            }
        }
        'Field' {
            $output += (" " + $Field.Keys + "=" + $Field.Values)
        }
    }
    $output
}
