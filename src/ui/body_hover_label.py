"""
Hover label UI for celestial bodies.
"""

from vpython import label, mag, scene, vector


class BodyHoverLabel:
    """
    Displays a label when hovering over a celestial body.
    """

    def __init__(self, bodies):
        self.bodies = bodies

        self.label = label(
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
        Updates the hover label based on the object under the mouse.
        """
        picked_object = scene.mouse.pick

        hovered_body = self._get_hovered_body(picked_object)

        if hovered_body is None:
            self.label.visible = False
            return

        self.label.pos = hovered_body.visual.pos
        self.label.text = self._build_label_text(hovered_body)
        self.label.visible = True

    def _get_hovered_body(self, picked_object):
        """
        Returns the body matching the picked VPython object.
        """
        for body in self.bodies:
            if body.visual == picked_object:
                return body

        return None

    def _build_label_text(self, body) -> str:
        """
        Builds the hover label text for a body.
        """
        speed = mag(body.velocity)

        return (
            f"{body.name}\n"
            f"Type: {body.type.value}\n"
            f"Speed: {speed:,.0f} m/s\n"
            f"Mass: {body.mass:.3e} kg\n"
            f"Radius: {body.radius:,.0f} m"
        )
