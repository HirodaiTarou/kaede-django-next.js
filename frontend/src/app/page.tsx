'use client';

import { useState, useEffect } from 'react';
import { helloApi } from '@/lib/api';
import UserList from '@/components/UserList';

export default function Home() {
  const [message, setMessage] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');

  const fetchHello = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await helloApi.getHello();
      setMessage(response.data.message);
    } catch (err) {
      setError('Failed to fetch hello message');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHello();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto py-8">
        <h1 className="text-3xl font-bold text-center mb-8">Kaede</h1>

        <div className="max-w-md mx-auto bg-white rounded-lg shadow-md p-6 mb-8">
          <h2 className="text-xl font-semibold mb-4">Backend Connection Test</h2>

          {loading && (
            <div className="text-blue-500">Loading...</div>
          )}

          {error && (
            <div className="text-red-500 mb-4">{error}</div>
          )}

          {message && (
            <div className="text-green-600 font-bold text-2xl mb-4">
              {message}
            </div>
          )}

          <button
            onClick={fetchHello}
            disabled={loading}
            className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 disabled:bg-gray-400"
          >
            {loading ? 'Loading...' : 'Test Connection'}
          </button>
        </div>

        <UserList />
      </div>
    </div>
  );
}
