from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        print(data)
        response = renderer_context.get("response")
        status_code = response.status_code if response else status.HTTP_200_OK
        
        if status_code >= 400:
            return super().render(
                {
                    "data": None,
                    "message": self._get_error_message(data),
                    "code": status_code
                }, 
                accepted_media_type, 
                renderer_context
            )

        if isinstance(data, dict) and data.get('results'):
            data = data.get('results')

        return super().render({
            "data": data,
            "message": "success",
            "code": status_code
        }, accepted_media_type, renderer_context)

    def _get_error_message(self, data):
        """
        Chuẩn hóa error message từ DRF
        """
        if isinstance(data, dict) and "detail" in data:
            return data["detail"]

        if isinstance(data, dict):
            return data

        return "Unexpected error"