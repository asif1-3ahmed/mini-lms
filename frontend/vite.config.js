// frontend/vite.config.js

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  // 🛑 CRITICAL FIX: Forces all asset paths (JS/CSS) to be relative 
  // (e.g., href="assets/index.css" instead of href="/assets/index.css")
  base: '', 
  plugins: [react()],
})
