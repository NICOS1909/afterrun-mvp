"""Service for generating AI feedback based on activity data and self-assessment."""
from typing import List

from src.models.activity import ActivityData, SelfAssessment, Feedback


class AIFeedbackService:
    """Service to generate structured AI feedback (with placeholder logic for MVP)."""
    
    @staticmethod
    def generate_feedback(
        activity_data: ActivityData,
        assessment: SelfAssessment
    ) -> Feedback:
        """
        Generate structured feedback based on activity data and self-assessment.
        
        NOTE: This is a placeholder implementation. In a production version,
        this would integrate with an actual AI/LLM service.
        
        Args:
            activity_data: Parsed activity data from GPX/TCX file
            assessment: User's self-assessment
            
        Returns:
            Feedback object with structured feedback
        """
        # Generate summary
        summary = AIFeedbackService._generate_summary(activity_data, assessment)
        
        # Generate context
        context = AIFeedbackService._generate_context(activity_data)
        
        # Generate data vs feeling analysis
        data_vs_feeling = AIFeedbackService._generate_data_vs_feeling(
            activity_data, assessment
        )
        
        # Generate reflection options
        reflection_options = AIFeedbackService._generate_reflection_options(
            activity_data, assessment
        )
        
        return Feedback(
            summary=summary,
            context=context,
            data_vs_feeling=data_vs_feeling,
            reflection_options=reflection_options
        )
    
    @staticmethod
    def _generate_summary(
        activity_data: ActivityData,
        assessment: SelfAssessment
    ) -> str:
        """Generate a summary of the run."""
        pace_formatted = activity_data.get_pace_formatted()
        duration_formatted = activity_data.get_duration_formatted()
        
        summary = (
            f"Du hast {activity_data.total_distance} km in {duration_formatted} "
            f"zurückgelegt mit einem durchschnittlichen Tempo von {pace_formatted} min/km."
        )
        
        if activity_data.elevation_gain:
            summary += f" Höhenmeter: {activity_data.elevation_gain} m."
        
        if activity_data.avg_heart_rate:
            summary += f" Durchschnittliche Herzfrequenz: {activity_data.avg_heart_rate} bpm."
        
        return summary
    
    @staticmethod
    def _generate_context(activity_data: ActivityData) -> str:
        """Generate context analysis."""
        # Placeholder logic for context analysis
        pace = activity_data.avg_pace
        distance = activity_data.total_distance
        
        if distance < 5:
            distance_context = "Dies war ein kurzer Lauf, ideal für Regeneration oder Techniktraining."
        elif distance < 10:
            distance_context = "Eine mittlere Distanz, gut für regelmäßiges Training."
        elif distance < 21:
            distance_context = "Eine längere Distanz, die Ausdauer und mentale Stärke erfordert."
        else:
            distance_context = "Eine beeindruckende lange Distanz, die viel Vorbereitung und Durchhaltevermögen zeigt."
        
        if pace < 4.5:
            pace_context = "Dein Tempo war sehr schnell."
        elif pace < 5.5:
            pace_context = "Dein Tempo war zügig."
        elif pace < 6.5:
            pace_context = "Dein Tempo war moderat."
        else:
            pace_context = "Dein Tempo war entspannt."
        
        return f"{distance_context} {pace_context}"
    
    @staticmethod
    def _generate_data_vs_feeling(
        activity_data: ActivityData,
        assessment: SelfAssessment
    ) -> str:
        """Compare objective data with subjective feeling."""
        feeling = assessment.feeling.lower()
        difficulty = assessment.difficulty.lower()
        
        # Placeholder logic for data vs feeling analysis
        analysis = "**Daten vs. Gefühl:**\n\n"
        
        if "gut" in feeling or "großartig" in feeling or "5" in feeling:
            if "leicht" in difficulty or "einfach" in difficulty:
                analysis += (
                    "Deine objektiven Daten und dein Gefühl stimmen überein. "
                    "Du warst gut erholt und der Lauf fühlte sich entsprechend an."
                )
            else:
                analysis += (
                    "Interessant: Die Daten zeigen eine solide Leistung, aber du hast den Lauf "
                    "als anstrengend empfunden. Das könnte auf Ermüdung oder andere Belastungen hinweisen."
                )
        elif "ok" in feeling or "mittel" in feeling or "3" in feeling:
            analysis += (
                "Du hattest einen durchschnittlichen Lauf. Solche Läufe sind normal und wichtig "
                "für den Trainingsaufbau."
            )
        else:
            if "schwer" in difficulty or "hart" in difficulty:
                analysis += (
                    "Der Lauf war heute herausfordernd. Das ist völlig normal und kann viele Gründe haben: "
                    "Wetter, Müdigkeit, oder einfach ein schwerer Tag. Wichtig ist, auf deinen Körper zu hören."
                )
            else:
                analysis += (
                    "Obwohl der Lauf nicht optimal lief, sind die Daten solide. "
                    "Manchmal stimmen Gefühl und Leistung nicht überein – das gehört dazu."
                )
        
        if assessment.notes:
            analysis += f"\n\nDeine Notizen: {assessment.notes}"
        
        return analysis
    
    @staticmethod
    def _generate_reflection_options(
        activity_data: ActivityData,
        assessment: SelfAssessment
    ) -> List[str]:
        """Generate reflection questions and options."""
        options = []
        
        # Distance-based reflections
        if activity_data.total_distance > 10:
            options.append(
                "Was hat dir geholfen, diese längere Distanz durchzuhalten?"
            )
        
        # Pace-based reflections
        if activity_data.avg_pace < 5.0:
            options.append(
                "Bei deinem schnellen Tempo: Wie war deine Atmung? Konntest du dich noch unterhalten?"
            )
        else:
            options.append(
                "Dein entspanntes Tempo ist gut für Grundlagenausdauer. Wie fühlte sich dein Energielevel an?"
            )
        
        # Heart rate reflections
        if activity_data.avg_heart_rate:
            if activity_data.avg_heart_rate > 160:
                options.append(
                    "Deine Herzfrequenz war relativ hoch. War das Tempo bewusst gewählt oder fühlte es sich anstrengend an?"
                )
            else:
                options.append(
                    "Deine Herzfrequenz war im moderaten Bereich. Perfekt für Ausdauertraining!"
                )
        
        # Feeling-based reflections
        feeling = assessment.feeling.lower()
        if "schlecht" in feeling or "schwer" in feeling or "1" in feeling or "2" in feeling:
            options.append(
                "Was könnte dir beim nächsten Mal helfen, dich besser zu fühlen? (z.B. mehr Schlaf, besseres Warm-up, anderes Timing)"
            )
        else:
            options.append(
                "Was hat heute besonders gut funktioniert? Versuche das beizubehalten!"
            )
        
        # General reflection
        options.append(
            "Was möchtest du beim nächsten Lauf anders oder genauso machen?"
        )
        
        return options
