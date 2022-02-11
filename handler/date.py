import time
from datetime import timedelta


class DateHelper:
    def consumed_time(self, start_time):
        """[it calculate the time that the function take to execute]

        Args:
            start_time ([time]): [the start time for the job]

        Returns:
            [String]: [the execution time that the function take to finished]
        """
        return str(timedelta(seconds=time.time() - start_time)).split('.')[0]
