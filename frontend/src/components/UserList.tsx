'use client';

import { useState, useEffect } from 'react';
import { userApi, User } from '@/lib/api';

export default function UserList() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await userApi.getUsers();
        setUsers(response.data);
      } catch (err) {
        setError('Failed to fetch users');
        console.error('Error fetching users:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) {
    return <div className="p-4">Loading users...</div>;
  }

  if (error) {
    return <div className="p-4 text-red-500">{error}</div>;
  }

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Users</h1>
      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <div className="grid gap-4">
          {users.map((user) => (
            <div key={user.id} className="border rounded-lg p-4 bg-white shadow">
              <h3 className="font-semibold text-lg">{user.username}</h3>
              <p className="text-gray-600">{user.email}</p>
              <p className="text-sm text-gray-500">
                {user.university_name} - {user.faculty} {user.department}
              </p>
              <p className="text-sm text-gray-500">
                Category: {user.category} | Admission Year: {user.admission_year}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}