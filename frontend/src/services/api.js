const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';

export async function checkHealth() {
    const response = await fetch(`${API_BASE_URL}/health`);
    if (!response.ok) throw new Error('Backend is not reachable');
    return response.json();
}

export async function generateReport(topic, language = 'fa') {
    const response = await fetch(`${API_BASE_URL}/generate-report`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic, language }),
    });

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `Server error (${response.status})`);
    }

    return response.json();
}

export async function getAllReports() {
    const response = await fetch(`${API_BASE_URL}/reports`);
    if (!response.ok) throw new Error('Failed to fetch reports');
    return response.json();
}

export async function getReport(id) {
    const response = await fetch(`${API_BASE_URL}/reports/${id}`);
    if (!response.ok) throw new Error('Report not found');
    return response.json();
}

export async function deleteReport(id) {
    const response = await fetch(`${API_BASE_URL}/reports/${id}`, {
        method: 'DELETE',
    });
    if (!response.ok) throw new Error('Failed to delete report');
    return response.json();
}

export async function updateReportTitle(id, title) {
    const response = await fetch(`${API_BASE_URL}/reports/${id}/title`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title }),
    });
    if (!response.ok) throw new Error('Failed to update title');
    return response.json();
}