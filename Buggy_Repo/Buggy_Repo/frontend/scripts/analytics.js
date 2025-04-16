const baseURL = "http://localhost:8001";

async function loadAnalytics() {
  try {
    const res = await fetch(`${baseURL}/analytics`);
    const data = await res.json();

    if (data.error) {
      throw new Error(data.error);
    }

    // ✅ Update statistics
    document.getElementById("itemCount").textContent = data.stats.item_count;
    document.getElementById("userCount").textContent = data.stats.user_count;
    document.getElementById("avgItemName").textContent = data.stats.avg_item_name_length.toFixed(2);
    document.getElementById("avgUserName").textContent = data.stats.avg_user_username_length.toFixed(2);
    document.getElementById("maxItemName").textContent = data.stats.max_item_name_length;
    document.getElementById("maxUserName").textContent = data.stats.max_user_username_length;

    // ✅ Display base64 image
    console.log("Plot value from server:", data.plot);
    const plotElement = document.getElementById("plot");

    if (data.plot && data.plot.startsWith("data:image")) {
      plotElement.src = data.plot;
    } else if (data.plot_base64) {
      plotElement.src = `data:image/png;base64,${data.plot_base64}`;
    } else {
      document.getElementById("analyticsError").textContent = "Plot data not available.";
    }

  } catch (error) {
    console.error("Failed to load analytics:", error);
    document.getElementById("analyticsError").textContent = "Failed to load analytics data. Please try again later.";
  }
}

loadAnalytics();
