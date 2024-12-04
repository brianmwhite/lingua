from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo


class TimezoneHelper:
    def set_timezone(self, timezone_name):
        self.timezone_full_name = timezone_name

    def get_timezone_full_name(self, timezone_abbreviation: str):
        # Determine the correct timezone path based on the input
        timezone_abbreviation = timezone_abbreviation.lower()
        if timezone_abbreviation == "et":
            timezone_path = "America/New_York"
        elif timezone_abbreviation == "ct":
            timezone_path = "America/Chicago"
        elif timezone_abbreviation == "mt":
            timezone_path = "America/Denver"
        elif timezone_abbreviation == "pt":
            timezone_path = "America/Los_Angeles"
        else:
            raise ValueError(
                "Unsupported timezone. Use 'ET' for Eastern Time or 'CT' for Central Time or 'MT' for Mountain Time or 'PT' for Pacific Time'."
            )
        return timezone_path

    def __format_utc_offset(self, offset_seconds: int):
        """Format UTC offset as HH:MM."""
        total_minutes = int(offset_seconds / 60)
        hours = total_minutes // 60
        minutes = abs(total_minutes % 60)  # Use abs to avoid negative signs in minutes
        return f"{hours:+02}:{minutes:02}"

    def get_next_timechange_date(self):
        if self.timezone_full_name:
            # Create a timezone object
            tz = ZoneInfo(self.timezone_full_name)

            # Get the current time in the specified timezone
            now = datetime.now(tz)

            # Get the current offset and DST status
            current_offset = now.utcoffset()

            # Find the next transition by iterating future dates
            days_ahead = 365  # Check up to one year in advance
            for day_offset in range(1, days_ahead + 1):
                future_date = now + timedelta(days=day_offset)
                future_offset = future_date.astimezone(tz).utcoffset()

                # Check if the offset has changed
                if future_offset != current_offset:
                    # Found the next transition
                    transition_date = future_date.replace(
                        hour=2, minute=0, second=0, microsecond=0
                    )
                    return transition_date
        else:
            return None

    def get_current_utc_time(self, offset_hours=0.0):
        """
        Returns the current date and time in UTC,
        with an optional offset added in hours.

        :param offset_hours: Integer number of hours to add to the current UTC time (default is 0).
        :return: Datetime object with the applied offset.
        """
        current_utc = datetime.now(timezone.utc)
        adjusted_time = current_utc + timedelta(hours=offset_hours)
        return adjusted_time

    def get_timezone_info(self):
        if self.timezone_full_name:
            # Create a timezone object
            tz = ZoneInfo(self.timezone_full_name)

            # Get the current time in the specified timezone
            now = datetime.now(tz)

            utc_offset_as_time = self.__format_utc_offset(
                now.utcoffset().total_seconds()
            )
            timezone_abbreviation = now.tzname()

            return f"{timezone_abbreviation} (UTC{utc_offset_as_time})"
        else:
            return None
