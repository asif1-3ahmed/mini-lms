import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  // CRITICAL FIX: Base URL for serving assets in production
  base: '/static/', 
})
