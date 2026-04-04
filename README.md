# 🤖 AI Interview Agent (Real-Time Voice-Based Interview System)

## 🚀 Overview

AI Interview Agent is a real-time, voice-enabled mock interview platform that simulates technical interviews using Large Language Models (LLMs). It evaluates candidate responses dynamically and provides structured feedback with scoring.

The system leverages speech-to-text, LLM-based evaluation, and WebSocket streaming to create an interactive interview experience.

---

## 🎯 Key Features

* 🎤 Real-time voice input using browser MediaRecorder API
* 🧠 AI-generated interview questions based on role
* ⚡ Live speech-to-text transcription using Whisper
* 🤖 LLM-based answer evaluation with scoring (0–10)
* 🔄 WebSocket-based streaming for low-latency interaction
* 📊 Structured feedback for each response
* 🌐 Full-stack application (React + FastAPI)

---

## 🏗️ Architecture

### Backend (FastAPI)

* Handles WebSocket connections for real-time audio streaming
* Uses **Faster-Whisper** for speech-to-text transcription
* Integrates with **LLM (via LangChain + Groq)** for:

  * Question generation
  * Answer evaluation
* Provides REST APIs for:

  * Question generation
  * Interview evaluation

### Frontend (React)

* Captures audio/video using MediaRecorder
* Streams audio chunks to backend
* Displays real-time transcription
* Manages interview flow (questions, navigation, submission)

---

## 🔧 Tech Stack

### AI / LLM

* LangChain
* Groq (LLM inference)
* Whisper (speech-to-text)

### Backend

* FastAPI
* WebSockets
* Python

### Frontend

* React.js
* JavaScript

### Infrastructure (extendable)

* Docker
* Kubernetes (Kyma deployment ready)

---

## ⚙️ How It Works

1. User enters target role
2. LLM generates 5 interview questions
3. User answers via voice
4. Audio is streamed to backend via WebSockets
5. Whisper converts speech → text
6. LLM evaluates answers and returns:

   * Score (0–10)
   * Feedback
7. Results displayed on UI

---

## 📡 API Endpoints

### Generate Questions

`POST /generate-questions`

### Evaluate Interview

`POST /evaluate-interview`

### WebSocket (Real-time transcription)

`/ws`

---

## 🧠 LLM Evaluation Logic

* Uses prompt-based evaluation:

  * Strict scoring (0–10)
  * Structured JSON output
* Handles parsing failures gracefully

---

## ⚡ Performance Considerations

* Uses async processing for non-blocking execution
* WebSocket streaming reduces latency
* Lightweight Whisper model for CPU efficiency

---

## 🚀 Future Enhancements

* Multi-agent evaluation system (LangGraph)
* Emotion / tone analysis
* Video-based behavioral feedback
* Resume-based adaptive questioning
* Scalable deployment with autoscaling (KEDA)

---

## 📌 Use Cases

* Mock interview preparation
* Skill assessment platforms
* AI-based HR screening tools
* EdTech applications

---

## 👨‍💻 Author

**Asif Shaikh**
AI Engineer | Platform Engineer

---
