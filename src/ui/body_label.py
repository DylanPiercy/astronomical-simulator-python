"""
Hover and pinned label UI for celestial bodies.
"""

from vpython import label, mag, scene, vector


class BodyLabel:
    """
    Displays hover labels and pinned labels for celestial bodies.
    """

    def __init__(self, bodies):
        self.bodies = bodies
        self.pinned_labels = {}

        self.hover_label = label(
            pos=vector(0, 0, 0),
            text="",
            visible=False,
            box=True,
            opacity=0.75,
            xoffset=20,
            yoffset=20,
            height=14,
        )

    def update(self) -> None:
        """
        Updates the hover label and all pinned labels.
        """
        self._update_hover_label()
        self._update_pinned_labels()

    def handle_click(self) -> None:
        """
        Pins or unpins a label for the clicked body.
        """
        clicked_body = self._get_body_from_object(scene.mouse.pick)

        if clicked_body is None:
            return

        if clicked_body in self.pinned_labels:
            self.pinned_labels[clicked_body].visible = False
            del self.pinned_labels[clicked_body]
            return

        self.pinned_labels[clicked_body] = label(
            pos=clicked_body.visual.pos,
            text=self._build_label_text(clicked_body),
            visible=True,
            box=True,
            opacity=0.75,
            xoffset=20,
            yoffset=20,
            height=14,
        )

    def _update_hover_label(self) -> None:
        """
        Updates the temporary hover label.
        """
        hovered_body = self._get_body_from_object(scene.mouse.pick)

        if hovered_body is None or hovered_body in self.pinned_labels:
            self.hover_label.visible = False
            return

        self.hover_label.pos = hovered_body.visual.pos
        self.hover_label.text = self._build_label_text(hovered_body)
        self.hover_label.visible = True

    def _update_pinned_labels(self) -> None:
        """
        Keeps pinned labels attached to their bodies.
        """
        for body, pinned_label in self.pinned_labels.items():
            pinned_label.pos = body.visual.pos
            pinned_label.text = self._build_label_text(body)

    def _get_body_from_object(self, picked_object):
        """
        Returns the celestial body matching the picked VPython object.
        """
        for body in self.bodies:
            if body.visual == picked_object:
                return body

        return None

    def _build_label_text(self, body) -> str:
        """
        Builds label text for a celestial body.
        """
        speed = mag(body.velocity)

        return (
            f"{body.name}\n"
            f"Type: {body.type.value}\n"
            f"Speed: {speed:,.0f} m/s\n"
            f"Mass: {body.mass:.3e} kg\n"
            f"Radius: {body.radius:,.0f} m"
        )
