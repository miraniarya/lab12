// ✅ Base URL of your backend API
const baseURL = "http://localhost:8001";

async function loadAnalytics() {
  try {
    // ✅ Fetch analytics data from the API
    const res = await fetch(`${baseURL}/analytics`);
    const data = await res.json();
    
    // ✅ Safely update statistics using the data object returned
    document.getElementById("itemCount").textContent = data.stats.item_count;
    document.getElementById("userCount").textContent = data.stats.user_count;
    document.getElementById("avgItemName").textContent = data.stats.avg_item_name_length.toFixed(2);
    document.getElementById("avgUserName").textContent = data.stats.avg_user_username_length.toFixed(2);
    document.getElementById("maxItemName").textContent = data.stats.max_item_name_length;
    document.getElementById("maxUserName").textContent = data.stats.max_user_username_length;
    
    // ✅ FIXED CODE:
    // Use the plot data directly as it now includes the complete data URI
    if (data.plot) {
      document.getElementById("plot").src = data.plot;
    } else if (data.plot_base64) {
      // Fallback for backward compatibility
      document.getElementById("plot").src = `data:image/png;base64,${data.plot_base64}`;
    }
  } catch (error) {
    // ✅ Handle errors gracefully by logging them
    console.error("Failed to load analytics:", error);
    // Optional: Show user feedback or fallback message in the UI
    document.getElementById("analyticsError").textContent = "Failed to load analytics data. Please try again later.";
  }
}

// ✅ Call the function on page load
loadAnalytics();
