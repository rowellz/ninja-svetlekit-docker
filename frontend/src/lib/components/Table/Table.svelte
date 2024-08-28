<script lang="ts">
    export let headers: string[] = [];
    export let data: any[] = [];

    // Transpose the data to align with headers
    $: transposedData = data[0] ? data[0].map((_, colIndex) => data.map(row => row[colIndex])) : [];
</script>

<head>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            overflow-x: auto; /* Makes table scrollable horizontally */
            display: block;
        }
    
        th, td {
            padding: 10px;
            text-align: left;
            border: 1px solid #ccc;
            background-color: #f8f8f8;
        }
    
        @media screen and (max-width: 768px) {
            th, td {
                padding: 5px; /* Smaller padding for smaller screens */
                font-size: 14px; /* Smaller font size for readability */
            }
        }
    
        @media screen and (max-width: 480px) {
            th, td {
                font-size: 12px; /* Even smaller font size for very small screens */
            }
        }
        select {
            font-size: inherit; /* Match the font size of the surrounding text */
            font-weight: bold; /* Optional: Match the font weight of the h1 */
            color: inherit; /* Match the text color of the surrounding text */
            border: none; /* Remove the default border */
            background-color: transparent; /* Make the background transparent */
            padding: 0.2em 0.5em; /* Add some padding */
            margin-left: 0.5em; /* Add some space to the left of the dropdown */
            cursor: pointer; /* Change cursor to pointer to indicate it's clickable */
        }
    </style>
</head>

<table>
    <thead>
        <tr>
            {#each headers as header}
                <th>{header}</th>
            {/each}
        </tr>
    </thead>
    <tbody>
        {#each transposedData as row, rowIndex}
            <tr>
                {#each row as cell, colIndex}
                    <td>
                        {#if headers[colIndex].toLowerCase().includes('pitcher_arsenal_clickable')}
                            <a href={cell} target="_blank">{row[colIndex - 2]}</a>
                        {:else if headers[colIndex].toLowerCase().includes('hitter_arsenal_clickable')}
                            <a href={cell} target="_blank">{row[colIndex - 6]}</a>
                        {:else}
                            {cell}
                        {/if}
                    </td>
                {/each}
            </tr>
        {/each}
    </tbody>
</table>