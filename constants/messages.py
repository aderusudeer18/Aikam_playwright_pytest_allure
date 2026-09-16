class ErrorMessages:
    INVALID_EMAIL = "Please enter a valid email address"
    INVALID_CREDENTIALS = "Invalid email or password"
    INVALID_CREDENTIALS_LOCATOR_TEXT = "text=Invalid email or password"

class AllureMessages:
    # Dashboard Page
    CLICK_ON_JOBS_ICON_STEP = "click on jobs icon"
    JOBS_ICON_CLICKED_SUCCESS = "Test case passed successfully:Jobs icon is clicked "
    CLICKED_ON_CREATE_JOB_STEP = "Clicked on Create job button in the jobs page"
    CLICKED_CREATE_JOB_SUCCESS = "Clicked 'Create Job' successfully"

    # Job Description Page
    WRITE_WITH_AI_STEP = "Enter into the Job description page and clicked on write with Ai button"
    WRITE_WITH_AI_SUCCESS = "Test case passed successfully:To generate Ai description Clicked on button to generate"
    INPUT_LLM_STEP = "Input has passed to LLM to generate description"
    INPUT_LLM_SUCCESS = "Test case passed successfully:Ai generated description for job "
    NEXT_BTN_DESC_STEP = "Job description generated successfully and Clicking on Next button"
    NEXT_BTN_DESC_SUCCESS = "Test case passed successfully:Ai generated the description & Next button is visible and clicked "

    # Publish Job Page
    PUBLISH_BTN_STEP = "After all steps Completed the Publish button is visible and clicked successfully"
    PUBLISH_BTN_SUCCESS = "Publish button clicked successfully"
    WAIT_JOBS_REDIRECT_STEP = "Wait until redirected to Jobs page"
    WAIT_JOBS_REDIRECT_SUCCESS = "Redirected to Jobs page successfully"

    # Super Admin Dashboard
    CREATE_ORG_STEP = "Create Organization"
    CREATE_ORG_SUCCESS = "Test case passed successfully: Clicked Create Organization button"
    CREATING_NEW_ORG_STEP = "creating new organisation"

class AllApplicantMessages:
    VERIFY_RESUMES_IMPORTED = "Verify resumes has been imported"
    VERIFY_RESUMES_IMPORTED_LOWER = "verify resumes has been imported"
    CLICK_EXPORT_EXCEL = "Clicking on Export excel button"
    APPLY_ADVANCE_FILTERS = "Applying advance filters to applicants"
    VERIFY_APPLICANT_PAGE_VISIBLE = "verify applicant page is visible"
    VERIFY_INTERVIEWS_TOGGLES = "verify interviews toggles given list"
    VERIFY_APPLICANTS_FILTERED = "verify applicants has been filtered based on advance filters"
    VERIFY_UNVIEWED_APPLICANTS = "verify unviewed applicants are visible"
    APPLY_EXCLUDE_KEYWORDS = "Applying advance filters to exclude keywords to applicants"
    RESET_ADVANCE_FILTERS = "reset your changes in the  advance filters "
    SEARCH_APPLICANT = "search by name or email,Phone number"

class JobsPageMessages:
    VERIFY_FILTER_JOB_TITLE = "verify filter using Job title"
    VERIFY_FILTER_JOB_CLIENT = "verify filter using Job title"
    VERIFY_FILTER_JOB_LOCATION = "verify filter using Job title"
    VERIFY_FILTER_JOB_POSTED_ON = "verify filter using Job title"
    VERIFY_FILTER_JOB_DEADLINE = "verify filter using Job title"
    VERIFY_JOB_BY_ID = "Verify job by job_id in Jobs page"

class ViewApplicantMessages:
    CLICK_VIEW_APPLICANTS = "Click View Applicants"

class TPOMessages:
    VERIFY_SEND_MAIL = "verify send mail to applicant"
    VERIFY_SHARE_APPLICANT_BTN = "verify share applicant button is visible to share applicant details"
    SELECT_APPLICANT_FOR_MAIL = "Select applicant for send mail: {applicant_name}"
    VERIFY_SEND_ICON_MAIL = "verify send icon to send mail to applicant"
    SELECT_APPLICANT_FOR_INTERVIEW = "Select applicant for interview: {applicant_name}"
    VERIFY_SCHEDULE_INTERVIEW = "verify to schedule interview to applicant"
    SELECT_JOB = "Select job: {job_name}"
    VERIFY_RESUMES_IMPORTED_TPO = "Verify resumes has imported "
    CLICK_CREATE_ASSESSMENT = "click on create assessment"
    SELECT_SKILL_ASSESSMENT = "Step 1: Select skill '{skill_name}'"
    ENTER_TITLE_PUBLISH_ASSESSMENT = "Step 2: Enter title '{assessment_title}' and publish"
    SELECT_APPLICANT = "Select applicant: {applicant_name}"

class SuperAdminMessages:
    EDIT_ORG_DETAILS = "edit org details"
    EDIT_ORG_EMAIL = "Edit org email"
    EDIT_ORG_NAME = "Edit org name"
    LOGIN_INVALID_EMAIL = "Login with invalid email"
    LOGIN_INVALID_PASSWORD = "Login with invalid invalid password"
    LOGIN_VALID_CREDENTIALS = "Login with valid email and password"

class ErrorLogMessages:
    FAILED_TO_CLICK_JOBS_ICON = "Failed to click jobs icon: "
    FAILED_TO_CLICK_CREATE_JOB = "Failed to click Create Job button: "
    FAILED_TO_CLICK_PUBLISH = "Failed to click Publish button: "
    FAILED_TO_REDIRECT_JOBS = "Failed to redirect to Jobs page after publishing: "
    LOGIN_FAILED_DASHBOARD_NOT_LOADED = "Login failed or Dashboard not loaded: "
    LOGIN_FAILED_AS_EXPECTED = "Login failed as expected. Error: "
    EXPECTED_ERROR_NOT_FOUND = "Expected error message not found: "

class LoginMessages:
    LOGIN_SUCCESS_DASHBOARD_VISIBLE = "Login successful and Dashboard is visible"
    LOGIN_SUCCESS_VALID_CREDENTIALS = "Test case passed successfully:Login has done with valid creditionals"
