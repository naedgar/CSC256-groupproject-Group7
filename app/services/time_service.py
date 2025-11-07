import requests
from datetime import datetime

class TimeService:
  def get_current_time(self):
      try:
          # Try external API first with proper headers
          headers = {
              'User-Agent': 'TaskTracker/1.0 (Python-requests)',
              'Accept': 'application/json'
          }
          # Try timeapi.io instead - more reliable for Python requests
          response = requests.get(
              "https://timeapi.io/api/Time/current/zone?timeZone=UTC", 
              timeout=3,
              headers=headers
          )
          response.raise_for_status()
          data = response.json()
          # timeapi.io returns different format
          return {
              "utc_datetime": data.get("dateTime"),
              "source": "TimeAPI.io (External)"
          }
      except Exception:
          # Fallback to local system time
          try:
              local_utc = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
              return {
                  "utc_datetime": local_utc,
                  "source": "System Time (Fallback)"
              }
          except Exception:
              return {"error": "Unable to fetch time from any source."}