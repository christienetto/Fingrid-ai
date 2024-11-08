package main

import (
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	// Setup CORS
	config := cors.DefaultConfig()
	config.AllowOrigins = []string{"http://localhost:3000"} // Your React app's URL
	r.Use(cors.New(config))

	// API routes
	r.GET("/api/posts", getPosts)
	r.POST("/api/posts", createPost)
	r.PUT("/api/posts/:id/vote", votePost)

	r.Run(":8080")
}

func getPosts(c *gin.Context) {
	// Implement fetching posts from database
}

func createPost(c *gin.Context) {
	// Implement creating a new post in database
}

func votePost(c *gin.Context) {
	// Implement upvoting/downvoting a post in database
}
