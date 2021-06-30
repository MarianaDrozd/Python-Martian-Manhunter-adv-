import re

if __name__ == "__main__":

    with open("django_success.log") as logfile:
        result = "".join(logfile.readlines())
        result = re.sub(r"\[\d*\/\w*\/\d*\s(\d{2}:?){3}\]", "[XX/XXX/XXXX XX:XX:XX]", result)

        result = re.sub(r'\/admin\/', '/*****/', result)
        with open("django_success_new.log", "a") as logfile_new:
            logfile_new.write(result)
