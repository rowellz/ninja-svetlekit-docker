<script lang="ts">
    import axios from 'axios';
    import { onMount } from 'svelte';

    interface Recipe {
        ingredients: string[];
        instructions: string[];
		grams_per_ingredient: Number[]
    }

    let responseData: Recipe | null = null;

    let userMessages: string[] = [];
    let aiMessages: Recipe[] = [];
    let combinedMessages: (string | Recipe)[] = [];
    let inputMessage: string = '';

    async function getRecipe() {
        userMessages = [...userMessages, inputMessage];
        combinedMessages = [...combinedMessages, inputMessage];

        try {
            const response = await axios.post('/api/chefy' + '?dish=' + inputMessage)
            responseData = response.data as Recipe;
            aiMessages = [...aiMessages, responseData];
            combinedMessages = [...combinedMessages, responseData];
            scrollToBottom();
        } catch (error) {
            console.error('Error making request:', error);
        }
		inputMessage = ''; 
    }

    function scrollToBottom() {
        const messagesContainer = document.getElementById('messages-container');
        if (messagesContainer) {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
    }

    onMount(() => {
        scrollToBottom();
    });
</script>

<head>
    <style>
        body {
            display: flex;
            flex-direction: column;
            height: 100vh;
            margin: 0;
        }
        #messages-container {
            flex: 1;
            overflow-y: auto;
            padding: 10px;
            display: flex;
            flex-direction: column;
            max-height: 800px;
        }
        .message {
            padding: 10px;
            margin: 5px 0;
            border-radius: 10px;
            max-width: 60%;
        }
        .message.even {
            align-self: flex-end;
            background-color: #e0e0e0;
        }
        .message.odd {
            align-self: flex-start;
            background-color: #c0c0c0;
        }
        .recipe {
            padding: 10px;
            margin: 5px 0;
            border-radius: 10px;
            max-width: 60%;
            background-color: #f0f0f0;
        }
        #input-container {
            display: flex;
            border-top: 1px solid #ccc;
        }
        #input-container input {
            flex: 1;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        #input-container button {
            margin-left: 10px;
            padding: 10px 20px;
            border: none;
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <div id="messages-container">
        <h3>Messages:</h3>
        {#each combinedMessages as message, index}
            {#if typeof message === 'string'}
                <div class="message {index % 2 === 0 ? 'even' : 'odd'}">
                    {message}
                </div>
            {:else}
                <div class="recipe">
                    <h4>Ingredients:</h4>
                    <ul>
                        {#each message.ingredients as ingredient, index}
                            {ingredient} | {message.grams_per_ingredient[index]} grams
							<br>
                        {/each}
                    </ul>
                    <h4>Instructions:</h4>
                    <ol>
                        {#each message.instructions as instruction}
                            {instruction}
							<br>
                        {/each}
                    </ol>
                </div>
            {/if}
        {/each}
    </div>
    <div id="input-container">
        <input type="text" bind:value={inputMessage} placeholder="Enter your message" />
        <button on:click={getRecipe}>Submit</button>
    </div>
</body>