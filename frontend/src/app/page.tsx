'use client';

import UserList from '@/components/UserList';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto py-8">
        <h1 className="text-3xl font-bold text-center">Kaede</h1>
        <UserList />
      </div>
    </div>
  );
}
