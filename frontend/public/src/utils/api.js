const API_BASE_URL = "https://api.airis.ai"; // Replace with your actual API URL

/**
 * Sends a GET request to the specified endpoint.
 *
 * @param {string} endpoint - The API endpoint to call.
 * @returns {Promise} - Resolves to the response data.
 */
export const fetchData = async (endpoint) => {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`);
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Fetch error:", error);
        throw error;
    }
};

/**
 * Sends a POST request with data to the specified endpoint.
 *
 * @param {string} endpoint - The API endpoint to call.
 * @param {object} data - The payload to send in the POST request.
 * @returns {Promise} - Resolves to the response data.
 */
export const postData = async (endpoint, data) => {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });
        if (!response.ok) {
            throw new Error(`Error posting data: ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Post error:", error);
        throw error;
    }
};

// Example usage
// fetchData("/analysis/results").then(data => console.log(data));
// postData("/analysis/start", { param: "value" }).then(data => console.log(data));
