from mcp.server.fastmcp import FastMCP
import psutil

# Create an instance of the MCP server
mcp = FastMCP("ProcessMonitor")

@mcp.tool()
def get_running_processes():
    """Scan OS processes and return list of process names."""
    procs = []
    for p in psutil.process_iter(['pid', 'name']):
        try:
            procs.append(p.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return list(set(procs))  # Return unique process names

if __name__ == "__main__":
    # Start the MCP server to listen for requests
    mcp.run()

    
