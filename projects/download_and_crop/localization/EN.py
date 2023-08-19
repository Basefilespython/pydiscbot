black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
violet = "\033[35m"
turquoise = "\033[36m"
white = "\033[37m"
st = "\033[37"

en_loc = {
   '0': f'''{'='*15}- Connection statuses -{'='*15}
{green}- 200 - Success!{white}
{'='*10} HTTP ERROR CODEs: {'='*10}
{red}- 400 - The script was unable to parse the URL.
- 401 - Authorization is needed ... you need to download it manually.
- 402 - Similar to 401, access after payment.
- 403 - Site/Browser/Anti-Virus denied you access to access this URL (perhaps VPN).
- 404 - Not found, or this is an outdated link.
{white}{'='*10} TIMEOUT ERROR CODEs: {'='*10}
{red}- 522 - The connection is not responding (maybe ILV blocked).
- 524 - TCP connection failed. (internal OS errors).
- 526 - Certificate blocking / ohm (rather different times, or parental control)
{white}{'='*10} OTHER: {'='*10}
{violet}- 101 - You are disconnected from the Internet.
- 102 - Error processing URL.{white}''',
   '1': 'Time',
   '2': 'Operating system',
   '3': 'Version',
   '4': 'You have the latest version of the script installed!',
   '5': 'Failed to get working directory.',
   '6':
   'Your OS is like Colab. All downloaded files will be downloaded to your Google Drive. Or rather, to the subfolder where this file is saved.',
   '7': 'RESTART THE SKIP RUNNING ENVIRONMENT.',
   '8': 'Base not found!',
   '9': 'You have an outdated version of the script installed!',
   '10': 'Install new version?',
   '11': 'Version check failed!',
   '12': 'Working directory',
   '13': 'Download to',
   '14': 'Number of images',
   '15': 'You aborted code execution',
   '16': 'Crop images in database?',
   '17': 'Directory',
   '18': 'Update version check failed!',
   "19": "Reload script.",
   "20": "The text below triggers a script termination notification.",
   "21": "Script completed",
   "22": "Done!",
   "23": "Start an endless loop",
   "24": "Downloading additional data",
   "25": "Main Script Version",
   "26": "Data Baze Version",
   "27": "Not Found",
   "28": "Script execution time",
   "29": "Start downloading additional data",
   "30": "You have an outdated version of the database installed!",
   "31": "Old software version",
   "32": "The previously installed module was not found.",
   "33": "Innovations"
}
