import requests
from datetime import datetime

class TimeService:
  # Mapping of friendly timezone names to IANA timezone identifiers
  TIMEZONE_MAP = {
      "UTC": "UTC",
      "Eastern": "America/New_York",
      "Central": "America/Chicago",
      "Mountain": "America/Denver",
      "Pacific": "America/Los_Angeles",
      "London": "Europe/London",
      "Beijing": "Asia/Shanghai"
  }

  def get_current_time(self, timezone="UTC"):
      # Convert friendly name to IANA timezone
      iana_timezone = self.TIMEZONE_MAP.get(timezone, "UTC")
      
      try:
          # Try external API first with proper headers
          headers = {
              'User-Agent': 'TaskTracker/1.0 (Python-requests)',
              'Accept': 'application/json'
          }
          # Try timeapi.io with the selected timezone
          url = f"https://timeapi.io/api/Time/current/zone?timeZone={iana_timezone}"
          print(f"DEBUG: Requesting URL: {url}")
          
          response = requests.get(
              url, 
              timeout=3,
              headers=headers
          )
          print(f"DEBUG: Response status: {response.status_code}")
          print(f"DEBUG: Response body: {response.text[:200]}")
          
          response.raise_for_status()
          data = response.json()
          # timeapi.io returns different format - normalize it
          datetime_str = data.get("dateTime", "")
          # Ensure the datetime has a Z suffix for UTC
          if datetime_str and not datetime_str.endswith('Z'):
              datetime_str = datetime_str + 'Z'
          
          return {
              "datetime": datetime_str,
              "utc_datetime": datetime_str,
              "timezone": timezone,
              "source": "TimeAPI.io (External)"
          }
      except Exception as e:
          # Log the error for debugging
          print(f"DEBUG: API request failed with error: {type(e).__name__}: {str(e)}")
          
          # Fallback to local system time
          try:
              local_utc = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
              return {
                  "datetime": local_utc,
                  "utc_datetime": local_utc,
                  "timezone": timezone,
                  "source": "System Time (Fallback)"
              }
          except Exception:
              return {"error": "Unable to fetch time from any source."}