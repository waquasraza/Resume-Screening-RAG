# API Documentation

## Base URL

http://localhost:8000

---

## Health Check

### GET /

Response

```json
{
  "status": "running"
}
```

---

## Upload Resume

### POST /resume/upload

Description

Uploads a resume PDF, extracts content, generates embeddings, and stores chunks in ChromaDB.

Request

Content-Type: multipart/form-data

Field:

file (PDF)

Response

```json
{
  "message": "Resume processed successfully",
  "file": "resume.pdf",
  "pages": 2,
  "chunks": 15,
  "stored_in_vector_db": true
}
```

---

## Ask Question

### POST /chat

Description

Performs semantic retrieval and generates AI-powered answers using resume content.

Request

```json
{
  "question": "Does this candidate have React Native experience?"
}
```

Response

```json
{
  "question": "Does this candidate have React Native experience?",
  "answer": "Yes. The candidate has experience developing Android applications using React Native."
}
```

---

## Error Responses

### 500 Internal Server Error

```json
{
  "detail": "Internal Server Error"
}
```

Common Causes

* Missing OpenAI API Key
* Invalid PDF
* ChromaDB Storage Error
* Embedding Generation Failure