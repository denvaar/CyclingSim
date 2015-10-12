Author: Denver Smith
Date: 10/12/2015

===============================
####### ABOUT #################
===============================

This program is a simple road-race
tracking system for cycling that helps
race officials, support teams, and 
spectators monitor cyclists.

This system meets the following requirments:

1. Subjects and observers. The subject's
   state is obsrved by any subscribed
   observers.
2. Race officials, support teams, and
   spectators are able to subscribe/
   unsubscribe to different racers.
        2.1. Appropriate data sent to each
             type of subscriber.
        2.2. User interface for each type
             of subscriber.
        2.2.2. Subscribe/unsubscribe.
        2.2.3. Emails are customized using
               a decorator pattern.
3. Design is captured using UML class,
   interaction, and state diagrams.
4. Unit tests of some key features.
5. The application may be ran and tested.

===============================
###### SETUP ##################
===============================

Requirments:

- Python2.7
- Twisted
- wxPython
- ObjectListView

This application uses Python's Twisted
package for networking. It can be found
here: https://twistedmatrix.com/trac/

The cross-platform GUI library, wxPython
is also used by this application.
http://www.wxpython.org/

ObjectListView is a wrapper around one of
the wxPython controls. Download information
found here: http://objectlistview.sourceforge.net/python/

Running the Application:

make sure that the PYTHONPATH variable is
set up correctly. You must add the path
to wxPython and ObjectListView to your python
path. Also add this project's root directory.

To run the application, type:

$ python frmMain.py


================================
##### FILES ####################
================================

src/version2/
    cheaterEmailer.py ---------- Part of decorator pattern, sends emails formatted for a race official.
    clsEmailInput.py  ---------- The form that a race official uses to set up email.
    clsJumbotron.py   ---------- The GUI for the jumbotron display.
    clsMain.py        ---------- The GUI for the main controller.
    clsPromoter.py    ---------- GUI for a race promoter.
    clsSpectator.py   ---------- GUI for setup of a race spectator.
    emailer.py        ---------- Emailer interface used in decorator pattern.
    fakeDatabase.py   ---------- The model, or place where my data is kept.
    frmMain.py        ---------- Application entry point.
    my_email.py       ---------- Part of decorator pattern.
    observer.py       ---------- Interface for an observer.
    promoter.py       ---------- Race promoter controller.
    raceofficial.py   ---------- Race official controller.
    racer.py          ---------- Model that represents a racer.
    spectator.py      ---------- Spectator controller.
    spectatorEmail.py ---------- Part of decorator pattern, sends emails formatted for a race spectator.
    subject.py        ---------- Interface for all subjects.
    tests/
        test_email.py         ----- Unit test for emails.
        test_fakeDatabase.py  ----- Unit test for in memory database.
        test_main.py          ----- Unit test for main window.
        test_observer.py      ----- Unit test for an observer.
        test_spectator.py     ----- Unit test for a spectator.
        test_subject.py       ----- Unit test for a subject




