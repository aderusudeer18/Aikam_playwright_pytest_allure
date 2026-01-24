from pages.import_resumes.import_resumes import ImportResume 


def test_import_resume(page):
    resume=ImportResume(page)
    resume.test_import_resumes()

