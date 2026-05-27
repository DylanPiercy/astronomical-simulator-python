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
        self.hovered_body = None

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
        self._update_hover_label()
        self._update_pinned_labels()

    def handle_click(self) -> None:
        clicked_body = self.hovered_body

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
        self.hovered_body = self._get_body_from_object(scene.mouse.pick)

        if self.hovered_body is None or self.hovered_body in self.pinned_labels:
            self.hover_label.visible = False
            return

        self.hover_label.pos = self.hovered_body.visual.pos
        self.hover_label.text = self._build_label_text(self.hovered_body)
        self.hover_label.visible = True

    def _update_pinned_labels(self) -> None:
        for body, pinned_label in self.pinned_labels.items():
            pinned_label.pos = body.visual.pos
            pinned_label.text = self._build_label_text(body)

    def _get_body_from_object(self, picked_object):
        for body in self.bodies:
            if body.visual == picked_object:
                return body

        return None

    def _build_label_text(self, body) -> str:
        speed = mag(body.velocity)

        label_lines = [
            body.name,
            f"Type: {body.type.value}",
        ]

        if body.parent_body is not None:
            parent_distance = mag(body.position - body.parent_body.position)

            label_lines.extend(
                [
                    f"Parent: {body.parent_body.name}",
                    f"Distance from parent: {parent_distance:.3e} m",
                ]
            )

        label_lines.extend(
            [
                f"Speed: {speed:,.0f} m/s",
                f"Velocity: {self._format_vector(body.velocity)} m/s",
                f"Mass: {body.mass:.3e} kg",
                f"Radius: {body.radius:,.0f} m",
            ]
        )

        return "\n".join(label_lines)

    def _format_vector(self, value: vector) -> str:
        return f"({value.x:.3e}, {value.y:.3e}, {value.z:.3e})"
