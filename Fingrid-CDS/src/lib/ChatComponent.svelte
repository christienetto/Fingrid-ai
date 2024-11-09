<!-- Save this as src/lib/ChatComponent.svelte -->
<script>
  let messages = [];
  let inputText = '';
  let isLoading = false;
  let chatBox;
  let previousMessageCount = 0;  // Add this line at the top with other variables

  
  async function handleSubmit() {
    if (!inputText.trim() || isLoading) return;
    
    isLoading = true;
    const userMessage = inputText;
    inputText = '';
    
    // Add user message immediately
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
      
      // Add AI response
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
    // Modified scroll logic
  $: if (chatBox && messages.length > previousMessageCount) {
    previousMessageCount = messages.length;
    setTimeout(() => {
      chatBox.scrollTop = chatBox.scrollHeight;
    }, 0);
  }
</script>

<div class="chat-wrapper">
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
    border: 1px solid #e2e8f0;
    border-radius: 0.5rem;
    background: white;
    overflow: hidden;
    width: 100%;
  }
  
  .messages {
    height: 400px;
    padding: 1rem;
    overflow-y: auto;
    background: #f8fafc;
  }
  
  .message {
    margin-bottom: 0.75rem;
    padding: 0.75rem;
    border-radius: 0.375rem;
    max-width: 80%;
  }
  
  .message.user {
    background: #e3f2fd;
    margin-left: auto;
  }
  
  .message.assistant {
    background: white;
    border: 1px solid #e2e8f0;
  }
  
  .message.error {
    background: #fee2e2;
    color: #dc2626;
  }
  
  .message-label {
    font-size: 0.875rem;
    font-weight: 500;
    margin-bottom: 0.25rem;
    display: block;
  }
  
  .message-content {
    white-space: pre-wrap;
    word-break: break-word;
  }
  
  .input-area {
    padding: 1rem;
    background: white;
    border-top: 1px solid #e2e8f0;
    display: flex;
    gap: 0.5rem;
  }
  
  textarea {
    flex: 1;
    min-height: 2.5rem;
    padding: 0.5rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
    resize: vertical;
  }
  
  textarea:disabled {
    background: #f1f5f9;
  }
  
  button {
    padding: 0.5rem 1rem;
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 0.375rem;
    cursor: pointer;
    font-weight: 500;
  }
  
  button:hover:not(:disabled) {
    background: #1d4ed8;
  }
  
  button:disabled {
    background: #94a3b8;
    cursor: not-allowed;
  }
  
  .loading {
    text-align: center;
    color: #64748b;
    padding: 0.5rem;
    font-style: italic;
  }
</style>