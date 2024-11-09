<script>
  let messages = [];
  let inputText = '';
  let isLoading = false;
  let chatBox;
  let previousMessageCount = 0;

  async function handleSubmit() {
    if (!inputText.trim() || isLoading) return;

    isLoading = true;
    const userMessage = inputText;
    inputText = '';

    messages = [...messages, {
      type: 'user',
      content: userMessage
    }];

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
      });

      if (!response.ok) throw new Error('Failed to get response');

      const data = await response.json();

      messages = [...messages, {
        type: 'assistant',
        content: data.response
      }];

    } catch (error) {
      messages = [...messages, {
        type: 'error',
        content: 'Failed to get response from AI'
      }];
    } finally {
      isLoading = false;
    }
  }

  $: if (chatBox && messages.length > previousMessageCount) {
    previousMessageCount = messages.length;
    setTimeout(() => {
      chatBox.scrollTop = chatBox.scrollHeight;
    }, 0);
  }
</script>

<div class="">
  <div 
    class="messages" 
    bind:this={chatBox}
  >
    {#each messages as message}
      <div class="message {message.type}">
        <span class="message-label">
          {message.type === 'user' ? 'You' : message.type === 'assistant' ? 'AI' : 'Error'}
        </span>
        <div class="message-content">
          {message.content}
        </div>
      </div>
    {/each}

    {#if isLoading}
      <div class="loading">AI is thinking...</div>
    {/if}
  </div>

  <div class="input-area">
    <textarea
      bind:value={inputText}
      placeholder="Type your message..."
      on:keydown={(e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          handleSubmit();
        }
      }}
      disabled={isLoading}
    ></textarea>
    <button 
      on:click={handleSubmit} 
      disabled={isLoading || !inputText.trim()}
    >
      Send
    </button>
  </div>
</div>

<style>
  .chat-wrapper {
    display: flex;
    flex-direction: column;
    border: 2px solid #52525b;
    border-radius: 1rem;
    background-color: #f8fafc;
    width: 100%;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
  }

  .messages {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center-aligns messages container */
  padding: 1rem;
  overflow-y: auto;
  background: #ffffff;
  border-bottom: 2px solid #52525b;
  color: #334155;
}

.message {
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: 0.5rem;
  max-width: 60%; /* Set max width for a centered appearance */
  font-size: 1rem;
  font-weight: 500;
}

.message.user {
  background: #e0f2fe;
  align-self: flex-end; /* Aligns user messages to the right */
  color: #1d4ed8;
}

.message.assistant {
  background: #f3f4f6;
  border: 1px solid #d1d5db;
  color: #1f2937;
  align-self: flex-start; /* Aligns AI messages to the left */
}


  .message.error {
    background: #fee2e2;
    color: #dc2626;
    border: 1px solid #f87171;
  }

  .message-label {
    font-size: 0.875rem;
    font-weight: 600;
    color: #64748b;
    margin-bottom: 0.5rem;
    display: block;
  }

  .message-content {
    white-space: pre-wrap;
    word-break: break-word;
  }

  .input-area {
    padding: 1rem;
    background: #ffffff;
    border-top: 2px solid #52525b;
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  textarea {
    flex: 1;
    min-height: 2.5rem;
    padding: 0.5rem;
    border: 2px solid #52525b;
    border-radius: 0.5rem;
    resize: vertical;
    font-size: 1rem;
    color: #334155;
    font-weight: 500;
  }

  textarea:disabled {
    background: #f3f4f6;
    color: #9ca3af;
  }

  button {
    padding: 0.5rem 1rem;
    background: #2563eb;
    color: #ffffff;
    border: none;
    border-radius: 0.5rem;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;
  }

  button:hover:not(:disabled) {
    background: #1e40af;
  }

  button:disabled {
    background: #94a3b8;
    cursor: not-allowed;
  }

  .loading {
    text-align: center;
    color: #6b7280;
    padding: 0.5rem;
    font-style: italic;
    font-weight: 500;
  }
</style>
