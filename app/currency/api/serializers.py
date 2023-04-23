from rest_framework import serializers

from currency.models import Rate, Source, ContactUs


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = (
            'name',
            'source_url',
        )


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'currency',
            'source',
            'created'
        )

    # works only for view, .create/.update override needed
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     source = representation.pop('source')
    #
    #     for key, value in source.items():
    #         representation[key] = value
    #
    #     return representation


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'created',
            'name',
            'email_from',
            'subject',
            'message',
        )

    def _send_mail(self, validated_data):
        subject = 'User ContactUs'
        message = f'''
                    Request from: {validated_data['name']}.
                    Reply to email: {validated_data['email_from']}.
                    Subject: {validated_data['subject']}.
                    Body: {validated_data['message']}.
                '''
        from currency.tasks import send_mail
        send_mail.delay(subject, message)

    def create(self, validated_data):
        self._send_mail(validated_data)
        return ContactUs.objects.create(**validated_data)
