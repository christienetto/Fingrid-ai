"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { ArrowUpIcon, ArrowDownIcon, SendIcon } from "lucide-react";

// Mock data structure
interface FeedbackPost {
  id: number;
  companyName: string;
  content: string;
  votes: number;
}

export default function CompanyFeedback() {
  const [posts, setPosts] = useState<FeedbackPost[]>([
    {
      id: 1,
      companyName: "Tech Corp",
      content: "Great work environment!",
      votes: 5,
    },
    {
      id: 2,
      companyName: "Startup Inc",
      content: "Exciting projects, but long hours.",
      votes: 3,
    },
  ]);
  const [newPost, setNewPost] = useState({ companyName: "", content: "" });
  const [sortBy, setSortBy] = useState<"newest" | "votes">("newest");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // In a real app, this would be an API call to the Go backend
    const newId = Math.max(...posts.map((p) => p.id)) + 1;
    setPosts([...posts, { ...newPost, id: newId, votes: 0 }]);
    setNewPost({ companyName: "", content: "" });
  };

  const handleVote = (id: number, increment: number) => {
    // In a real app, this would be an API call to the Go backend
    setPosts(
      posts.map((post) =>
        post.id === id ? { ...post, votes: post.votes + increment } : post
      )
    );
  };

  const sortedPosts = [...posts].sort((a, b) =>
    sortBy === "newest" ? b.id - a.id : b.votes - a.votes
  );

  return (
    <div className="container mx-auto p-4 max-w-3xl">
      <h1 className="text-3xl font-bold mb-6">Company Feedback Forum</h1>

      <Card className="mb-6">
        <CardHeader>
          <CardTitle>Submit New Feedback</CardTitle>
        </CardHeader>
        <form onSubmit={handleSubmit}>
          <CardContent className="space-y-4">
            <Input
              placeholder="Company Name"
              value={newPost.companyName}
              onChange={(e) =>
                setNewPost({ ...newPost, companyName: e.target.value })
              }
              required
            />
            <Textarea
              placeholder="Your feedback..."
              value={newPost.content}
              onChange={(e) =>
                setNewPost({ ...newPost, content: e.target.value })
              }
              required
            />
          </CardContent>
          <CardFooter>
            <Button type="submit">
              <SendIcon className="mr-2 h-4 w-4" /> Submit Feedback
            </Button>
          </CardFooter>
        </form>
      </Card>

      <div className="mb-4 flex justify-between items-center">
        <h2 className="text-2xl font-semibold">Feedback Posts</h2>
        <select
          className="border rounded p-2"
          value={sortBy}
          onChange={(e) => setSortBy(e.target.value as "newest" | "votes")}
        >
          <option value="newest">Sort by Newest</option>
          <option value="votes">Sort by Votes</option>
        </select>
      </div>

      {sortedPosts.map((post) => (
        <Card key={post.id} className="mb-4">
          <CardHeader>
            <CardTitle>{post.companyName}</CardTitle>
          </CardHeader>
          <CardContent>
            <p>{post.content}</p>
          </CardContent>
          <CardFooter className="flex justify-between items-center">
            <div className="flex items-center space-x-2">
              <Button
                variant="outline"
                size="icon"
                onClick={() => handleVote(post.id, 1)}
              >
                <ArrowUpIcon className="h-4 w-4" />
              </Button>
              <span className="font-bold">{post.votes}</span>
              <Button
                variant="outline"
                size="icon"
                onClick={() => handleVote(post.id, -1)}
              >
                <ArrowDownIcon className="h-4 w-4" />
              </Button>
            </div>
          </CardFooter>
        </Card>
      ))}
    </div>
  );
}
