"""
AfterRun – Dein Laufcoach
A Streamlit MVP app for analyzing running activities and providing structured feedback.
"""
import streamlit as st
from src.services.file_parser import FileParserService
from src.services.ai_feedback import AIFeedbackService
from src.models.activity import SelfAssessment
from src.utils.file_utils import save_uploaded_file, cleanup_old_files


def init_session_state():
    """Initialize session state variables."""
    if 'activity_data' not in st.session_state:
        st.session_state.activity_data = None
    if 'file_uploaded' not in st.session_state:
        st.session_state.file_uploaded = False
    if 'assessment_completed' not in st.session_state:
        st.session_state.assessment_completed = False


def display_header():
    """Display the app header."""
    st.title("🏃 AfterRun – Dein Laufcoach")
    st.markdown("""
    Willkommen bei AfterRun! Lade deine Laufaktivität hoch, teile deine Einschätzung, 
    und erhalte strukturiertes Feedback zu deinem Training.
    """)
    st.markdown("---")


def file_upload_section():
    """Handle file upload section."""
    st.header("📁 1. Aktivität hochladen")
    st.markdown("Lade deine GPX- oder TCX-Datei von deinem Lauf hoch.")
    
    uploaded_file = st.file_uploader(
        "Wähle eine Datei aus",
        type=['gpx', 'tcx'],
        help="Unterstützte Formate: GPX, TCX"
    )
    
    if uploaded_file is not None:
        with st.spinner("Datei wird verarbeitet..."):
            # Save the uploaded file
            file_path = save_uploaded_file(uploaded_file)
            
            if file_path:
                # Parse the activity file
                activity_data = FileParserService.parse_activity_file(file_path)
                
                if activity_data:
                    st.session_state.activity_data = activity_data
                    st.session_state.file_uploaded = True
                    st.success("✅ Datei erfolgreich hochgeladen und verarbeitet!")
                    
                    # Display activity summary
                    display_activity_summary(activity_data)
                else:
                    st.error("❌ Fehler beim Verarbeiten der Datei. Bitte überprüfe das Dateiformat.")
            else:
                st.error("❌ Fehler beim Speichern der Datei.")


def display_activity_summary(activity_data):
    """Display a summary of the parsed activity data."""
    st.subheader("📊 Aktivitäts-Übersicht")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Distanz", f"{activity_data.total_distance} km")
    with col2:
        st.metric("Dauer", activity_data.get_duration_formatted())
    with col3:
        st.metric("Durchschnittstempo", f"{activity_data.get_pace_formatted()} min/km")
    
    if activity_data.elevation_gain or activity_data.avg_heart_rate:
        col4, col5 = st.columns(2)
        
        if activity_data.elevation_gain:
            with col4:
                st.metric("Höhenmeter", f"{activity_data.elevation_gain} m")
        
        if activity_data.avg_heart_rate:
            with col5:
                st.metric("Ø Herzfrequenz", f"{activity_data.avg_heart_rate} bpm")


def self_assessment_section():
    """Handle self-assessment questionnaire section."""
    if not st.session_state.file_uploaded:
        return
    
    st.markdown("---")
    st.header("📝 2. Selbsteinschätzung")
    st.markdown("Beantworte drei kurze Fragen zu deinem Lauf:")
    
    with st.form("assessment_form"):
        # Question 1: How did you feel?
        feeling = st.select_slider(
            "Wie hast du dich während des Laufs gefühlt?",
            options=["1 - Sehr schlecht", "2 - Schlecht", "3 - Ok", "4 - Gut", "5 - Großartig"],
            value="3 - Ok"
        )
        
        # Question 2: How hard was it?
        difficulty = st.select_slider(
            "Wie schwer war der Lauf für dich?",
            options=["Sehr leicht", "Leicht", "Mittel", "Schwer", "Sehr schwer"],
            value="Mittel"
        )
        
        # Question 3: Additional notes
        notes = st.text_area(
            "Zusätzliche Notizen (optional)",
            placeholder="z.B. Wetterbedingungen, besondere Herausforderungen, mentale Verfassung...",
            max_chars=500
        )
        
        submitted = st.form_submit_button("Feedback generieren", use_container_width=True)
        
        if submitted:
            assessment = SelfAssessment(
                feeling=feeling,
                difficulty=difficulty,
                notes=notes
            )
            
            st.session_state.assessment = assessment
            st.session_state.assessment_completed = True


def feedback_section():
    """Display AI-generated feedback section."""
    if not st.session_state.assessment_completed:
        return
    
    st.markdown("---")
    st.header("💡 3. Dein Feedback")
    
    with st.spinner("Feedback wird generiert..."):
        # Generate feedback
        feedback = AIFeedbackService.generate_feedback(
            st.session_state.activity_data,
            st.session_state.assessment
        )
        
        # Display Summary
        st.subheader("📋 Zusammenfassung")
        st.info(feedback.summary)
        
        # Display Context
        st.subheader("🎯 Kontext")
        st.write(feedback.context)
        
        # Display Data vs Feeling
        st.subheader("🔍 Daten vs. Gefühl")
        st.markdown(feedback.data_vs_feeling)
        
        # Display Reflection Options
        st.subheader("💭 Reflexionsfragen")
        st.markdown("Nimm dir einen Moment Zeit, um über diese Fragen nachzudenken:")
        for i, option in enumerate(feedback.reflection_options, 1):
            st.markdown(f"{i}. {option}")
        
        # Success message
        st.success("✅ Feedback erfolgreich generiert!")
        
        # Reset button
        if st.button("🔄 Neue Analyse starten", use_container_width=True):
            st.session_state.clear()
            st.rerun()


def display_footer():
    """Display footer information."""
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p><strong>Hinweis:</strong> Diese App dient nur zu Informationszwecken. 
    Sie erstellt keine Trainingspläne und gibt keine medizinischen Ratschläge.</p>
    <p>AfterRun MVP © 2024</p>
    </div>
    """, unsafe_allow_html=True)


def main():
    """Main application function."""
    # Configure page
    st.set_page_config(
        page_title="AfterRun – Dein Laufcoach",
        page_icon="🏃",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state
    init_session_state()
    
    # Clean up old files (optional, runs in background)
    cleanup_old_files()
    
    # Display sections
    display_header()
    file_upload_section()
    self_assessment_section()
    feedback_section()
    display_footer()


if __name__ == "__main__":
    main()
