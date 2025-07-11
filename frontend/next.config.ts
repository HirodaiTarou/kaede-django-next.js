import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  env: {
    NEXT_PUBLIC_API_URL: process.env.NODE_ENV === 'production' 
      ? process.env.NEXT_PUBLIC_API_URL || 'https://your-app.onrender.com/api'
      : 'http://localhost:8000/api'
  },
  output: 'standalone',
  trailingSlash: true,
};

export default nextConfig;
