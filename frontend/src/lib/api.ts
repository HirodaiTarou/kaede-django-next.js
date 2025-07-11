import axios, { AxiosResponse } from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

export const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export interface User {
  id: number;
  username: string;
  email: string;
  university_name: string;
  category: string;
  faculty: string;
  department: string;
  admission_year: number;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export const userApi = {
  getUsers: (): Promise<AxiosResponse<PaginatedResponse<User>>> => api.get('/users/'),
  getUser: (id: number) => api.get<User>(`/users/${id}/`),
};

export const helloApi = {
  getHello: () => api.get<{ message: string }>('/hello/'),
};