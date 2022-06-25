import http
import json

from django.http import JsonResponse

from webapp.models import Ad


def set_status_accept(request):
    if request.method == "POST" and request.user.is_staff:
        try:
            if request.body:
                body = json.loads(request.body)
                if body["status"] == "accept":
                    Ad.objects.get(pk=body["id"]).set_status_approve()
                    return JsonResponse(data={"status": "success"}, status=http.HTTPStatus.OK)
        except:
            return JsonResponse(data={"status": "failed"}, status=http.HTTPStatus.NOT_FOUND)


def set_status_reject(request):
    if request.method == "POST" and request.user.is_staff:
        try:
            if request.body:
                body = json.loads(request.body)
                if body["status"] == "reject":
                    Ad.objects.get(pk=body["id"]).set_status_reject()
                    return JsonResponse(data={"status": "success"}, status=http.HTTPStatus.OK)
        except:
            return JsonResponse(data={"status": "failed"}, status=http.HTTPStatus.NOT_FOUND)