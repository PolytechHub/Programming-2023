import pytest
from app import function

@pytest.mark.parametrize(
        "event, userdata, message, ans",
        [
            ("GREETING", "Bromley 78", '', 
                "For 78: Hello, Bromley. Welcome to our nice service!"
            ),
            ("NOTIFY", "Bromley 78", 
                "Configure the following ringtone options: choose a ringtone from the list (e.g., Silent, Default, etc.) then tap OK, Done, or Apply. If you have any questions, please contact our service center for clarification.",
                "For 78: Sir/Madam Bromley, regarding your application: Configure the following ringtone options: choose a ringtone from the list (e.g., Silent, Default, etc.) then tap OK, Done, or Apply. If you have any questions, please contact our service center for ..."
            ),
            ("DENIAL", "Bromley 78",
                "Unfortunately, we have to decline your application due to insufficient evidence regarding the case.",
                "For 78: Sir/Madam Bromley, regarding your application: Unfortunately, we have to decline your application due to insufficient evidence regarding the case."
            ),
            ("SOMETHINGWRONG", "Bromley 78", '', "wrong event"),
            ("NOTIFY", "Bromley 78", 
                "Your application is being processed",
                "For 78: Sir/Madam Bromley, regarding your application: Your application is being processed"
            )
        ]
)
def test(event, userdata, message, ans):
    assert function(event, userdata, message) == ans

if __name__ == '__main__':
    pytest.main(['-v', 'test.py'])