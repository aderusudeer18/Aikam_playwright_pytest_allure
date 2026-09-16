class LoginLocators:
    EMAIL_INPUT_TYPE = '//input[@type="email"]'
    EMAIL_INPUT_ID = '//input[@id="email"]'
    PASSWORD_INPUT = '//input[@type="password"]'
    LOGIN_BTN = '//div[text()="Login"]'

class DashboardLocators:
    JOBS_ICON = 'svg.lucide-briefcase-business'
    CREATE_JOB_BTN = "//button[contains(text(),'Create Job')]"

class JobDescriptionLocators:
    WRITE_WITH_AI_BTN = "//button[contains(.,'Write with AI')]"
    PROMPT_TEXTAREA = "//textarea[@placeholder='Enter your prompt']"
    GENERATE_AI_BTN = "//button[contains(text(),'Generate with AI')]"
    NEXT_BTN_NAME = "Next"

class JobKeyDetailsLocators:
    CREATE_JOB_BTN = '//button[contains(text(),"Create Job")]'
    DESCRIPTION_TEXTAREA = "//textarea[@placeholder='Example: We are hiring a frontend developer with 3+ years experience in React who can build scalable SaaS applications']"
    CREATE_AI_BTN = "//button[contains(text(),'Create with AI')]"
    JOB_TITLE_INPUT = '//input[@placeholder="Title that describes the role"]'
    OPTIONS_ROLE = '[role="option"]'
    JOB_TYPE_COMBOBOX = '//button[@role="combobox"]'
    WORKPLACE_TYPE_BTN = '//button[@type="button"]'
    LOCATION_CONTAINER = "//label[normalize-space()='Job Location']/following-sibling::*[1]"
    LOCATION_INPUT = "input[type='text']:not([disabled])"
    DROPDOWN_BTN = "//button[@type='button']"
    MIN_EXP_INPUT = '//input[@placeholder="Min"]'
    MAX_EXP_INPUT = '//input[@placeholder="Max"]'
    MIN_SALARY_INPUT = '//input[@name="minsalary"]'
    MAX_SALARY_INPUT = '//input[@name="maxsalary"]'
    DATE_BUTTON = "//label[text()='Target Deadline']/following::button[1]"
    CALENDAR_DIALOG = "//div[@role='dialog']"
    MONTH_YEAR_HEADER = "//div[@aria-live='polite'] | //h6 | //div[contains(@class,'Header')]"
    NAV_BUTTONS = "//button"
    PUBLISH_BTN = "//button[contains(text(),'Publish')]"

class PreviewLocators:
    NEXT_BTN = '//button[@type="button"]'

class PublishLocators:
    PUBLISH_BTN = '//button[@name="publish"]'

class ScheduleInterviewLocators:
    SCHEDULE_AI_INTERVIEW_BTN = '//button[contains(text(),"Schedule AI Interview")]'
    VIDEO_INTERVIEW_RADIO = '//label[contains(text(),"Video Interview")]'
    CODING_ASSESSMENT_RADIO = '//label[contains(text(),"Coding Assessment")]'
    NEXT_BTN = "//button[contains(text(),'Next')]"

class SendMailLocators:
    SEND_MAIL_ICON = 'button:has(svg.lucide-mail)'
    CONTINUE_WITH_AIKAM_EMAIL = '//*[contains(text(),"Continue with aikam email")]'
    SEND_EMAIL_BTN = "//button[contains(text(),'Send Email')]"

class ShareApplicantLocators:
    SEND_ICON = 'button:has(svg.lucide-send)'

class SignUpLocators:
    SIGN_UP_LINK = '//a[contains(text(),"Sign up")]'
    EMAIL_INPUT = '//input[@name="email"]'
    SUBMIT_BTN = '//button[@type="submit"]'

class ImportResumeLocators:
    IMPORT_RESUMES_SPAN = "//span[contains(text(),'Import Resumes')]"

class ViewApplicantLocators:
    VIEW_APPLICANTS_BTN = "//p[contains(text(),'View Applicants')]"

class TpoDashboardLocators:
    JOBS_ICON = "svg.lucide-briefcase-business"

class TpoCreateAssessmentLocators:
    CREATE_ASSESSMENT_BTN = "//button[contains(text(),'Create Assessment')]"
    SEARCH_INPUT = 'input[placeholder="Search skill..."]'
    NEXT_BTN = 'button:has-text("Next")'
    TITLE_INPUT = 'input[placeholder="Title that describes the role"]'
    PUBLISH_BTN = 'button:has-text("Publish")'

class TpoJobPageLocators:
    COMBOBOX = '//button[@role="combobox"]'
    SEARCH_BOX = '//input[@placeholder="Search Assessment Title"]'
    VIEW_JOB_BTN = '//button[contains(text(),"View Assessment") or contains(text(),"View Job")]'

class TpoImportResumesLocators:
    IMPORT_RESUMES_SPAN = "//*[contains(text(),'Import Resumes')]"
    ERROR_TOAST = "text=Error uploading file"
    APPLICANT_LOCATOR_TEMPLATE = "//*[contains(text(),'{}')]"

class TpoAllApplicantLocators:
    CHECKBOXES = "input[type='checkbox']"
    COMBOBOX_CLOSED = '//div[@data-state="closed"]'
    SEND_EMAIL_BTN = "//button[contains(text(),'Send Email')]"

class TpoScheduleInterviewLocators:
    SCHEDULE_AI_INTERVIEW_BTN = '//button[contains(text(),"Schedule AI Interview")]'
    CONTINUE_EMAIL_BTN = 'button:has-text("Continue with aikam email")'
    VIDEO_CHECKBOX = 'button#video'
    CODING_CHECKBOX = 'button#coding'

class TpoSendMailLocators:
    SEND_MAIL_ICON = 'button:has(svg.lucide-mail)'
    CONTINUE_EMAIL_BTN = '//*[contains(text(),"Continue with aikam email")]'
    SEND_EMAIL_BTN = "//button[contains(text(),'Send Email')]"

class TpoShareApplicantLocators:
    SEND_ICON = 'button:has(svg.lucide-send)'

class TpoViewApplicantLocators:
    VIEW_APPLICANTS_BTN = "//p[contains(text(),'View Applicants')]"
