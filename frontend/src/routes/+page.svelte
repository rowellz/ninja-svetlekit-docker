<script lang="ts">
    import axios from 'axios';
    import { onMount } from 'svelte';

    let responseData: { [key: string]: any }[] | null = null;
    let userMessages: string[] = [];
    let aiMessages: string[] = [];
    let combinedMessages: string[] = [];
    let inputMessage: string = '';

    async function squidward() {
        userMessages = [...userMessages, inputMessage];
        combinedMessages = [...combinedMessages, inputMessage];
        inputMessage = '';
        try {
            const response = await axios.post('/api/openai', {
                user_messages: userMessages,
                ai_messages: aiMessages
            }, {
                headers: {
                    'accept': '*/*',
                    'Content-Type': 'application/json'
                }
            });
            responseData = response.data;
            const aiMessage = responseData?.toString() || '';
            aiMessages = [...aiMessages, aiMessage];
            combinedMessages = [...combinedMessages, aiMessage];
            console.log('Combined Messages:', combinedMessages); 
            scrollToBottom();
        } catch (error) {
            console.error('Error making request:', error);
        }
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
            <div class="message {index % 2 === 0 ? 'even' : 'odd'}">
                {message}
            </div>
        {/each}
    </div>
    <div id="input-container">
        <input type="text" bind:value={inputMessage} placeholder="Enter your message" />
        <button on:click={squidward}>Submit</button>
    </div>
</body>